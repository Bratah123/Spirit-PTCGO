"""STUB: effect not implemented — do not guess mechanics.
Bonsly (DP1 #71): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import baby_evolution, baby_evolution_condition, fake_tears

card = PokemonCardDef(
    guid="5d04b7ae-2585-5a9e-a050-078122ae9c0f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bonsly.Name",
    display_name="Bonsly",
    searchable_by=["Bonsly", "Basic", "Bonsly"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=438,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Sudowoodo from your hand onto Bonsly (this counts as evolving Bonsly) and remove all damage counters from Bonsly.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=baby_evolution_condition('Sudowoodo'),
            effect=baby_evolution('Sudowoodo'),
        ),
        Attack(
            title="Fake Tears",
            game_text="Flip a coin. If heads, your opponent can't play any Trainer cards from his or her hand during your opponent's next turn, and any damage done to Bonsly by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={},
            effect=fake_tears(30),
        ),
    ],
)