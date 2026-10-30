"""STUB: effect not implemented — do not guess mechanics.
Nidoking δ (EX15 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import dark_horn_discard_snipe_bench
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="89dcdbd4-1bc9-5f72-abcd-ece58ee77d56",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking δ",
    searchable_by=["Nidoking \u03b4", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=34,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=snipe_attack(30, pool='any'),
        ),
        Attack(
            title="Dark Horn",
            game_text="You may discard a Basic Pok\u00e9mon or Evolution card from your hand. If you do, choose 1 of your opponent's Benched Pok\u00e9mon and do 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=dark_horn_discard_snipe_bench(60, 30),
        ),
    ],
)