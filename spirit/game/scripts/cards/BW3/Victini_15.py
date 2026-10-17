from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, count_bench


card = PokemonCardDef(
    guid="50b2fb5f-f383-5c91-bdba-e6d58feaea58",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victini.Name",
    display_name="Victini",
    searchable_by=["Victini", "Basic", "Victini"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="BW3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V-create",
            game_text="If you have 4 or fewer Benched Pok\u00e9mon, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bonus_if(
                lambda ctx: count_bench("mine")(ctx) >= 5,
                0, else_nothing=True,
            ),
        ),
    ],
)
