"""STUB: effect not implemented — do not guess mechanics.
Palkia-EX (XY9 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="d891a91d-0f55-577b-94c7-f3414805cf62",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaEX.Name",
    display_name="Palkia-EX",
    searchable_by=["Palkia-EX", "Basic", "EX", "PalkiaEX"],
    subtypes=["Basic", "EX"],
    collector_number=31,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=484,
    abilities=[
        Attack(
            title="Aqua Turbo",
            game_text="Search your deck for 2 Water Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pearl Hurricane",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 4},
            damage=120,
            # STUB: attack effect not implemented
            effect=snipe_attack(30, also_base=True),
        ),
    ],
)