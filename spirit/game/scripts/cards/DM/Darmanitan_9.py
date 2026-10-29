from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dm import (
    darmani_hands,
    heat_assist,
)

card = PokemonCardDef(
    guid="fa48510e-6146-5674-9c87-0778335176a2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Heat Assist",
            game_text="Attach up to 3 Fire Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            effect=heat_assist,
        ),
        Attack(
            title="Darmani-Hands",
            game_text="Flip 4 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=darmani_hands,
        ),
    ],
)