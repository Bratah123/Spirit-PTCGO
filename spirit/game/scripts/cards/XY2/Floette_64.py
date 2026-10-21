from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive


class _FlowerVeil(Passive):
    """Each of your Grass Pokemon in play gets +20 HP."""
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        return 20 if PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []) else 0


card = PokemonCardDef(
    guid="8bb76b9b-52b9-57d0-bd5e-9044cdaf6a20",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1", "Floette"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Flower Veil",
            game_text="Each of your Grass Pok\u00e9mon in play gets +20 HP.",
            passive=_FlowerVeil(),
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
        ),
    ],
)