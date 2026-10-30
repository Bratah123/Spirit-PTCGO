from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    cheer_up_draw, negative_ion_reduce, bolt_snipe_by_ability,
)


card = PokemonCardDef(
    guid="27b95710-0fea-55e8-8969-8c938e47823d",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=312,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Draw a card. If you have Plusle in play, draw 2 cards instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cheer_up_draw("Plusle"),
        ),
        Attack(
            title="Negative Ion",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pokémon is reduced by 10 (before applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=negative_ion_reduce(10),
        ),
        Attack(
            title="Power Bolt",
            game_text="Choose 1 of your opponent's Pokémon that has any Poké-Powers. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=bolt_snipe_by_ability(30, AbilityTypes.POKE_POWER),
        ),
    ],
)
