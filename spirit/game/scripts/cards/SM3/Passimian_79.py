from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import intentional_grounding

card = PokemonCardDef(
    guid="b381e864-d1b3-560c-bfc0-7f1eca539c60",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Intentional Grounding",
            game_text="Discard a Pok\u00e9mon Tool card from your hand. If you don't, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            effect=intentional_grounding,
        ),
    ],
)
