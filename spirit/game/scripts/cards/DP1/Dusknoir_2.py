"""STUB: effect not implemented — do not guess mechanics.
Dusknoir (DP1 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import hard_feelings
from spirit.game.card_effects.dp import dark_palm, dark_palm_condition, poke_power_condition
from spirit.game.data_utils import Activations

card = PokemonCardDef(
    guid="a77fd8f0-b733-5fd4-8bf3-efa9a79ff5ce",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusknoir.Name",
    display_name="Dusknoir",
    searchable_by=["Dusknoir", "Stage 2", "Dusknoir"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclops.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Dark Palm",
            game_text="Once during your turn (before your attack), if your opponent has 4 or more Benched Pok\u00e9mon, you may choose 1 of them and shuffle that Pok\u00e9mon and all cards attached to it into his or her deck. This power can't be used if Dusknoir if affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            condition=poke_power_condition(dark_palm_condition),
            activation=Activations.ONCE_PER_TURN,
            effect=dark_palm(),
        ),
        Attack(
            title="Hard Feelings",
            game_text="Put 5 damage counters on the Defending Pok\u00e9mon. Then, count the number of Prize cards your opponent has taken and put that many damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=hard_feelings(5),
        ),
    ],
)