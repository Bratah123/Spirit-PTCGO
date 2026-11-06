from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_prizes_remaining


card = PokemonCardDef(
    guid="d529a2b2-37f1-52bd-ab12-b4ceabe94890",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=436,
    abilities=[
        Attack(
            title="Payback",
            game_text="If your opponent has only 1 Prize card left, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_prizes_remaining('opponent')(ctx) == 1, 60),
        ),
    ],
)