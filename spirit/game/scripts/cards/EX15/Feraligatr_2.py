"""STUB: effect not implemented — do not guess mechanics.
Feraligatr δ (EX15 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import battle_aura_delta_boost, drag_off_optional


card = PokemonCardDef(
    guid="ff38b741-441d-56b9-99ee-5c56b449c09d",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr δ",
    searchable_by=["Feraligatr \u03b4", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=160,
    abilities=[
        Ability(
            title="Battle Aura",
            game_text="Each of your Pok\u00e9mon that has \u03b4 on its card does 10 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=battle_aura_delta_boost(10),
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=drag_off_optional(),
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)