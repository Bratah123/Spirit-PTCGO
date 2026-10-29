from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm4 import empty_light, symbiont_gx


card = PokemonCardDef(
    guid="1b8ed6ca-a6fb-5d71-8f3c-9aa2ee5f3b13",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NihilegoGX.Name",
    display_name="Nihilego-GX",
    searchable_by=["Nihilego-GX", "Basic", "GX", "Ultra Beast", "NihilegoGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=49,
    set_code="SM4",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=793,
    abilities=[
        Ability(
            title="Empty Light",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may leave both Active Pok\u00e9mon Confused and Poisoned.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=empty_light,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Symbiont-GX",
            game_text="Add the top 2 cards of your opponent's deck to their Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=symbiont_gx,
        ),
    ],
)