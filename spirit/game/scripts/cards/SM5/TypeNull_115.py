from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage

card = PokemonCardDef(
    guid="31eca897-3558-5602-bc5a-04b3276dd8d0",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    display_name="Type: Null",
    searchable_by=["Type: Null", "Basic", "TypeNull"],
    subtypes=["Basic"],
    collector_number=115,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=772,
    abilities=[
        Attack(
            title="Merciless Strike",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if(has_damage(), 30),
        ),
        Attack(
            title="Headbang",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)