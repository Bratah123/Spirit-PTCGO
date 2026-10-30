from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import no_resistance_passive
from spirit.game.card_effects.support_common import heal_targets


card = PokemonCardDef(
    guid="bfaeb3d5-656e-526a-aaae-ff013d28bc44",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Withering Dust",
            game_text="As long as Beautifly is in play, do not apply Resistance for all Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=no_resistance_passive(when=lambda calc, _carrier: calc.to_active),
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Parallel Gain",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon, including Beautifly.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=heal_targets(10, scope="each_own"),
        ),
    ],
)
