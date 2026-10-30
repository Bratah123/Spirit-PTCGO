"""STUB: effect not implemented — do not guess mechanics.
Luxray (DP1 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import gleam_eyes_on_evolve, lightning_star
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="81dae511-2968-59cf-ae6a-bae2de4ab93f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Gleam Eyes",
            game_text="Once during your turn, when you play Luxray from your hand to evolve 1 of your Pok\u00e9mon, you may look at your opponent's hand. If your opponent's Bench isn't full, choose 1 Basic Pok\u00e9mon from your opponent's hand, and put it onto his or her Bench. Then, switch it with the Defending Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=gleam_eyes_on_evolve(),
        ),
        Attack(
            title="Lightning Star",
            game_text="Move all Lightning Energy attached to Luxray to 1 of your Benched Pok\u00e9mon. (Ignore this effect if you don't have any Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=80,
            effect=lightning_star(),
        ),
    ],
)