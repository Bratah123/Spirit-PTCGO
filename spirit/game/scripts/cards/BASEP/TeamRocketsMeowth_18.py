from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, flip_damage


card = PokemonCardDef(
    guid="fb39866f-97e4-5d09-bfc8-8209a92272ef",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    display_name="Team Rocket's Meowth",
    searchable_by=["Team Rocket's Meowth", "Basic", "TeamRocketsMeowth"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Miraculous Comeback",
            game_text="Flip a number of coins equal to the number of Pok\u00e9mon in play. This attack does 10 damage times the number of heads. Then Team Rocket's Meowth does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_damage(
                coins_from=count_in_play(side="both"),
                per_heads=10,
                per_tails_self=10,
            ),
        ),
    ],
)
