from spirit.game.card_effects.ex import energy_press_active
"""STUB: effect not implemented — do not guess mechanics.
Dark Magcargo (EX7 #38): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="c758979d-7d74-57cf-89da-02d5bccc9acc",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagcargo.Name",
    display_name="Dark Magcargo",
    searchable_by=["Dark Magcargo", "Stage 1", "DarkMagcargo"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Energy Press",
            game_text="Does 10 damage plus 10 more damage for each basic Energy card attached to all of your Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=energy_press_active(),
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=snipe_attack(40, pool='any'),
        ),
    ],
)