from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import total_command
from spirit.game.card_effects.pokemon import rock_crush

card = PokemonCardDef(
    guid="b7f863e1-1bcc-5a93-a590-4103ec9ef783",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=81,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Attack(
            title="Total Command",
            game_text="This attack does 20 damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=total_command,
        ),
        Attack(
            title="Whirlpool",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=rock_crush,
        ),
    ],
)
