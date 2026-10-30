from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ex import force_opponent_switch


card = PokemonCardDef(
    guid="d27c7cf6-e558-5527-a652-55fbbb1b092a",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon, if any.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=force_opponent_switch(),
        ),
        Attack(
            title="Thunder",
            game_text="Flip a coin. If tails, Raikou does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_damage(tails_self_damage=20),
        ),
    ],
)
