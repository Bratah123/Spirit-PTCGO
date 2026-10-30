"""STUB: effect not implemented — do not guess mechanics.
Slowbro (EX10 #13): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import dual_armor_if_energy, parallel_gain_heal

card = PokemonCardDef(
    guid="b64fc42a-4bd7-53d6-8c65-26ee548c2279",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Dual Armor",
            game_text="As long as Slowbro has any Psychic Energy attached to it, Slowbro is both Water and Psychic type.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dual_armor_if_energy(PokemonTypes.PSYCHIC, PokemonTypes.WATER, PokemonTypes.PSYCHIC),
        ),
        Attack(
            title="Parallel Gain",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon (including Slowbro).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=parallel_gain_heal(1),
        ),
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)