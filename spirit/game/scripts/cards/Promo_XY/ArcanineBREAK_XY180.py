"""STUB: effect not implemented — do not guess mechanics.
Arcanine BREAK (Promo_XY #XY180): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="75a5d6de-2178-5225-b76a-3ec79a0b0272",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArcanineBREAK.Name",
    display_name="Arcanine BREAK",
    searchable_by=["Arcanine BREAK", "BREAK", "ArcanineBREAK"],
    subtypes=["BREAK"],
    collector_number=180,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    family_id=59,
    abilities=[
        Attack(
            title="Turbo Flame",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)