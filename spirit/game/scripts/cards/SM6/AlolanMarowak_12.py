from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.sm6 import alolan_club

card = PokemonCardDef(
    guid="36355701-69d0-515b-90cc-2125f06b3242",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMarowak.Name",
    display_name="Alolan Marowak",
    searchable_by=["Alolan Marowak", "Stage 1", "AlolanMarowak"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Attack(
            title="Limbo Limbo",
            game_text="Search your deck for up to 2 basic Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={},
            effect=search_attach_energy(is_basic_energy_card, count=2),
        ),
        Attack(
            title="Alolan Club",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play that has Alolan in its name.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=alolan_club,
        ),
    ],
)
