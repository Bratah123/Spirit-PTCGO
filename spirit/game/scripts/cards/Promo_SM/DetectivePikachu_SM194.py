from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.smp import brilliant_deduction

card = PokemonCardDef(
    guid="8d12c765-9791-5e71-acb4-f29dae03db1b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DetectivePikachu.Name",
    display_name="Detective Pikachu",
    searchable_by=["Detective Pikachu", "Basic", "DetectivePikachu"],
    subtypes=["Basic"],
    collector_number=194,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title="Brilliant Deduction",
            game_text="Look at the top 4 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=brilliant_deduction,
        ),
    ],
)