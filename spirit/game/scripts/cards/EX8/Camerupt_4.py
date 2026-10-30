"""STUB: effect not implemented — do not guess mechanics.
Camerupt (EX8 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import back_burner_attach, split_bomb_snipe


card = PokemonCardDef(
    guid="812a638c-b91c-51ae-8041-114731b4d13e",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1", "Camerupt"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Back Burner",
            game_text="Search your discard pile for up to 2 basic Energy cards and attach them to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=back_burner_attach(),
        ),
        Attack(
            title="Split Bomb",
            game_text="Choose 2 of your opponent's Pok\u00e9mon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=split_bomb_snipe(),
        ),
    ],
)