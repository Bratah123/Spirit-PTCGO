from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage


card = PokemonCardDef(
    guid="eaacf081-692e-559c-a638-cf1056082586",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=95,
    abilities=[
        Attack(
            title="Crush",
            game_text="Flip a number of coins equal to the amount of Energy attached to Onix. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=20),
        ),
    ],
)
