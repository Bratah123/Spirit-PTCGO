from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.sm5 import more_prizes_remaining, suns_eclipse_gx

card = PokemonCardDef(
    guid="2d392e0c-7bef-5ca0-bd2c-a86aae4127a1",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozmaGX.Name",
    display_name="Dusk Mane Necrozma-GX",
    searchable_by=["Dusk Mane Necrozma-GX", "Basic", "GX", "Ultra Beast", "DuskManeNecrozmaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=90,
    set_code="SM5",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=800,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Meteor Tempest",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=3),
        ),
        Attack(
            title="Sun's Eclipse-GX",
            game_text="You can use this attack only if you have more Prize cards remaining than your opponent. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 3},
            damage=250,
            effect=suns_eclipse_gx,
            condition=more_prizes_remaining,
        ),
    ],
)