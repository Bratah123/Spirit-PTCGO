from spirit.game.card_effects.ex import dump_and_draw
"""STUB: effect not implemented — do not guess mechanics.
Magmar (EX7 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ca66624c-f13f-5cb2-b744-9fed8693beb4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Dump and Draw",
            game_text="Discard up to 2 Energy cards from your hand. Then, draw 2 cards for each Energy card you discarded.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dump_and_draw(),
        ),
        Attack(
            title="Flame Tail",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)