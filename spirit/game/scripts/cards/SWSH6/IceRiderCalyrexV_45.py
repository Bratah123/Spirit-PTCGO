from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="a3e293a3-d82d-5cb8-a193-94e749a8b9f3",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    display_name="Ice Rider Calyrex V",
    searchable_by=["Ice Rider Calyrex V", "Basic", "V", "IceRiderCalyrexV"],
    subtypes=["Basic", "V"],
    collector_number=45,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=898,
    abilities=[
        Attack(
            title="Pierce",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Glacial Lance",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)