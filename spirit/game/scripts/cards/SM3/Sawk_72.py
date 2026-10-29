from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import brick_break, quick_guard_attack

card = PokemonCardDef(
    guid="1834d977-16a9-5458-aaa4-cbdafeb1cd89",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Quick Guard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon during your opponent's next turn. This Pok\u00e9mon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            locks_next_turn=True,
            effect=quick_guard_attack,
        ),
        Attack(
            title="Brick Break",
            game_text="This attack's damage isn't affected by Resistance or any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=brick_break,
        ),
    ],
)
