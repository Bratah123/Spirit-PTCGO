from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="0a68d9b5-d14f-5c65-a307-a557db78ab29",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    display_name="Lt. Surge's Voltorb",
    searchable_by=["Lt. Surge's Voltorb", "Basic", "LtSurgesVoltorb"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Bouncing Ball",
            game_text="Flip a coin. If tails, Lt. Surge's Voltorb does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_damage(tails_self_damage=10),
        ),
    ],
)
