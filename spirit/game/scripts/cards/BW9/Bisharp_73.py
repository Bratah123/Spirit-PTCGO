from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, active_is
from spirit.game.card_effects.trainers import is_dragon_pokemon


card = PokemonCardDef(
    guid="6507bcdc-8b18-598e-a04b-746da849e045",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1", "Team Plasma", "Bisharp"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=73,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Dragon Slayer",
            game_text="If the Defending Pok\u00e9mon is a Dragon Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bonus_if(active_is(is_dragon_pokemon), 40),
        ),
    ],
)