"""STUB: effect not implemented — do not guess mechanics.
Crobat (EX5 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import flutter_trick, triple_poison

card = PokemonCardDef(
    guid="cd385bbe-6c44-52bd-907b-a034ec3a3435",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Flutter Trick",
            game_text="Flip a coin. If heads, look at your opponent's hand and choose 1 card. Your opponent discards the card you chose.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flutter_trick(),
        ),
        Attack(
            title="Triple Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 3 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=triple_poison(),
        ),
    ],
)