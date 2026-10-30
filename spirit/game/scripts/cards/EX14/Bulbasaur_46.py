"""STUB: effect not implemented — do not guess mechanics.
Bulbasaur (EX14 #46): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import growth_attach


card = PokemonCardDef(
    guid="2e029f18-ae99-52a4-a348-a3bd26bbeac9",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic", "Bulbasaur"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="EX14",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Growth",
            game_text="Attach a Grass Energy card from your hand to Bulbasaur.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=growth_attach(PokemonTypes.GRASS),
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)