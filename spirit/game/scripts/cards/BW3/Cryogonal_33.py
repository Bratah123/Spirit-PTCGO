from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack, remove_self_from_play

card = PokemonCardDef(
    guid="7f8c299a-09ef-5aeb-9550-bed55bbc9f82",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic", "Cryogonal"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Ice Chain",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=gust_attack(damage_before=0),
        ),
        Attack(
            title="Frost Vanish",
            game_text="You may return this Pok\u00e9mon and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=remove_self_from_play("hand", optional=True),
        ),
    ],
)
