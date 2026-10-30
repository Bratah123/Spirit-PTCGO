from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, condition_attack
from spirit.game.attributes import SpecialConditions


card = PokemonCardDef(
    guid="3a94ddd1-6209-5383-9a4f-14d27055f00d",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Psybeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
