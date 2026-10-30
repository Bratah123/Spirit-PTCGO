"""STUB: effect not implemented — do not guess mechanics.
Mightyena (EX8 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import pull_away_to_4, seek_out_any


card = PokemonCardDef(
    guid="78d78bc4-cccd-5ece-b584-6fc9e1555920",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1", "Mightyena"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Seek Out",
            game_text="Search your deck for 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=seek_out_any(),
        ),
        Attack(
            title="Pull Away",
            game_text="If your opponent has 5 or more cards in his or her hand, your opponent discards a number of cards until your opponent has 4 cards left in his or her hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=pull_away_to_4(),
        ),
    ],
)