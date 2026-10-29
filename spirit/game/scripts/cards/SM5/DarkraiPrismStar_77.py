from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm5 import nightmare_star

card = PokemonCardDef(
    guid="407ce2d8-ce50-5543-a1bb-7c4d89ade0bf",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiPrismStar.Name",
    display_name="Darkrai {*}",
    searchable_by=["Darkrai {*}", "Basic", "Prism Star", "DarkraiPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=77,
    set_code="SM5",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Ability(
            title="Nightmare Star",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach 2 Darkness Energy cards from your hand to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=nightmare_star,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Abyssal Sleep",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.DARKNESS: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, checkup_coins=2),
        ),
    ],
)