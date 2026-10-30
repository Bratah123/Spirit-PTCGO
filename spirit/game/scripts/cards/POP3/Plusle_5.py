from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import cheer_up_draw, bolt_snipe_by_ability


card = PokemonCardDef(
    guid="260b5405-c27e-5d15-8ab0-1b51ecb09489",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=311,
    abilities=[
        Attack(
            title="Cheer Up",
            game_text="Draw a card. If you have Minun in play, draw 2 cards instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cheer_up_draw("Minun"),
        ),
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 10 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
        Attack(
            title="Body Bolt",
            game_text="Choose 1 of your opponent's Pokémon that has any Poké-Bodies. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=bolt_snipe_by_ability(30, AbilityTypes.POKE_BODY),
        ),
    ],
)
