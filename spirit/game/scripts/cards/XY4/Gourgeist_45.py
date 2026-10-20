from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.attacks_common import damage_per


class _Gourgantic(Passive):
    """With any Grass Energy attached, this Pokemon's maximum HP is 200."""
    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return 0
        if not any(is_energy_card(c) and energy_provides_type(c, PokemonTypes.GRASS.value)
                   for c in pokemon.children):
            return 0
        printed = pokemon.attribute_originals.get(AttrID.HP.value, 0) or 0
        return max(0, 200 - printed)


card = PokemonCardDef(
    guid="a1301206-89f2-5bf1-bc77-1b8b4b15d88a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name",
    display_name="Gourgeist",
    searchable_by=["Gourgeist", "Stage 1", "Gourgeist"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Ability(
            title="Gourgantic",
            game_text="If this Pok\u00e9mon has any Grass Energy attached to it, its maximum HP is 200.",
            passive=_Gourgantic(),
        ),
        Attack(
            title="Horror Note",
            game_text="This attack does 10 damage times the number of cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=damage_per(lambda ctx: len(ctx.hand()), 10),
        ),
    ],
)