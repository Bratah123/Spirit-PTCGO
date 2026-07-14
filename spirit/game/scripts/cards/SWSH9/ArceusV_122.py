from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

trinity_charge = search_attach_energy(
    is_basic_energy_card, count=3,
    target_pred=lambda p: is_pokemon_v(p.archetype_id),
    prompt="Choose up to 3 basic Energy cards to attach to your Pokémon V.",
)

card = PokemonCardDef(
    guid="ba8e44a9-5efd-5592-ac85-f1f69a39ae5c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    display_name="Arceus V",
    searchable_by=["Arceus V", "Basic", "V", "ArceusV"],
    subtypes=["Basic", "V"],
    collector_number=122,
    set_code="SWSH9",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Attack(
            title="Trinity Charge",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pokémon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=trinity_charge,
        ),
        Attack(
            title="Power Edge",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)
