from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack

card = PokemonCardDef(
    guid="a21484ae-0b01-5b8b-82ef-85cd896f5633",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorV.Name",
    display_name="Rhyperior V",
    searchable_by=["Rhyperior V", "Basic", "V", "RhyperiorV"],
    subtypes=["Basic", "V"],
    collector_number=95,
    set_code="SWSH3",
    rarity=Rarities.RareHoloV,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=464,
    abilities=[
        Attack(
            title="Drill Run",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=discard_opponent_energy_attack(),
        ),
        Attack(
            title="Heavy Rock Artillery",
            game_text="During your next turn, this Pok\u00e9mon can't use Heavy Rock Artillery.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=210,
            locks_next_turn=True,
        ),
    ],
)