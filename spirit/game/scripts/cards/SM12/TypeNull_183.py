from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="a49ae1a7-2289-513e-a6e4-1d16e864ed2e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=["Type: Null", "Basic", "TypeNull"],
    subtypes=["Basic"],
    collector_number=183,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)