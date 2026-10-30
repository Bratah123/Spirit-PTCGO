"""STUB: effect not implemented — do not guess mechanics.
Stantler (EX10 #32): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import confuse_if_evolved


card = PokemonCardDef(
    guid="352efb0f-fcad-57a9-bb1a-36a5cf57f6cb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stantler.Name",
    display_name="Stantler",
    searchable_by=["Stantler", "Basic", "Stantler"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="EX10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=234,
    abilities=[
        Attack(
            title="Screechy Voice",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=confuse_if_evolved(),
        ),
        Attack(
            title="Push Away",
            game_text="Look at your opponent's hand, choose a Trainer card you find there, and discard it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=confuse_if_evolved(),
        ),
    ],
)