from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.attacks_common import bonus_if


card = PokemonCardDef(
    guid="02de805e-6912-59f7-87bc-f34be6e7f73a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZygardeEX.Name",
    display_name="Zygarde-EX",
    searchable_by=["Zygarde-EX", "Basic", "EX", "ZygardeEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Land's Pulse",
            game_text="If there is any Stadium card in play, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.stadium_in_play() is not None, 20),
        ),
        Attack(
            title="Cell Storm",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=heal_attack(30),
        ),
        Attack(
            title="Land's Wrath",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)