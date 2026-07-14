from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="2f68f1dc-961e-57e9-b5aa-2fe845f67ac8",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boldore.Name",
    display_name="Boldore",
    searchable_by=["Boldore", "Stage 1", "Boldore"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    family_id=524,
    abilities=[
        Attack(
            title="Protect",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
