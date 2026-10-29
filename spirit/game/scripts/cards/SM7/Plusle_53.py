from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    draw_for_everybody,
)

card = PokemonCardDef(
    guid="76211cf9-f3b1-56ea-a936-fde4fa0278d1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=311,
    abilities=[
        Attack(
            title="Draw for Everybody",
            game_text="Shuffle your hand into your deck. Then, draw a card for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_for_everybody,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)