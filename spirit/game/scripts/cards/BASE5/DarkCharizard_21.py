from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import continuous_fireball


card = PokemonCardDef(
    guid="d2604600-a3ae-5e9a-ba27-fe9398a71ea3",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharizard.Name",
    display_name="Dark Charizard",
    searchable_by=["Dark Charizard", "Stage 2", "DarkCharizard"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Nail Flick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Continuous Fireball",
            game_text="Flip a number of coins equal to the number of Fire Energy cards attached to Dark Charizard. This attack does 50 damage times the number of heads. Discard a number of Fire Energy cards attached to Dark Charizard equal to the number of heads.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            damage_operator="x",
            effect=continuous_fireball,
        ),
    ],
)
