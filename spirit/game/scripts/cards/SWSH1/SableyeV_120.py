from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.session.effects import is_trainer_card

card = PokemonCardDef(
    guid="59eb1d89-ad28-5923-8d84-e867c63358cf",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SableyeV.Name",
    display_name="Sableye V",
    searchable_by=["Sableye V", "Basic", "V", "SableyeV"],
    subtypes=["Basic", "V"],
    collector_number=120,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=302,
    abilities=[
        Attack(
            title="Lode Search",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=recover_from_discard(is_trainer_card, count=1, minimum=1,
                                        reveal=False, to="hand"),
        ),
        Attack(
            title="Crazy Claws",
            game_text="This attack does 60 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 60, base=10),
        ),
    ],
)