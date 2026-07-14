from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class WarmingUpPassive(Passive):
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return 0
        for child in carrier.children:
            definition = def_for(getattr(child, "archetype_id", None) or "")
            if definition is not None and definition.display_name == "Burning Scarf":
                return 100
        return 0


card = PokemonCardDef(
    guid="5484aedf-88dd-5122-b7db-ed05a849e5e6",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Warming Up",
            game_text="If this Pok\u00e9mon has a Burning Scarf attached, it gets +100 HP.",
            passive=WarmingUpPassive(),
        ),
        Attack(
            title="Fire Mane",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)