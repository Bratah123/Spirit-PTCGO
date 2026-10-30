"""STUB: effect not implemented — do not guess mechanics.
Milotic (EX5 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import distorted_wave, healing_shower

card = PokemonCardDef(
    guid="9d517409-590f-5351-bcc1-2df96838fc1e",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Healing Shower",
            game_text="Once during your turn, when you play Milotic from your hand to evolve 1 of your Pok\u00e9mon, you may remove all damage counters from all of your Pok\u00e9mon and your opponent's Pok\u00e9mon (excluding Pok\u00e9mon-ex).",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            effect=healing_shower(),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Distorted Wave",
            game_text="Before doing damage, remove 3 damage counters from the Defending Pok\u00e9mon (all if there are less than 3).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=distorted_wave(3),
        ),
    ],
)