from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="36d88b05-9a07-5c2f-8c54-7254e61e512e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OnixGX.Name",
    display_name="Onix-GX",
    searchable_by=["Onix-GX", "Basic", "GX", "OnixGX"],
    subtypes=["Basic", "GX"],
    collector_number=36,
    set_code="HF",
    rarity=Rarities.RareHoloGX,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 4},
            damage=150,
        ),
        Attack(
            title="Rocky Avalanche-GX",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance). (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=protect_next_turn(reduce=100),
        ),
    ],
)
