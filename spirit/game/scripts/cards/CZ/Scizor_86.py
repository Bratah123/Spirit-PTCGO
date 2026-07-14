from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, bonus_if, active_is
from spirit.game.session.effects import is_basic_pokemon

card = PokemonCardDef(
    guid="66f9da28-828f-5625-8278-048a8d4908bd",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Dangerous Claws",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 80 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            effect=bonus_if(active_is(is_basic_pokemon), 80),
        ),
    ],
)