from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="8523b874-1d31-51cb-86ad-af56f008c716",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuraludonV.Name",
    display_name="Duraludon V",
    searchable_by=["Duraludon V", "Basic", "V", "DuraludonV"],
    subtypes=["Basic", "V"],
    collector_number=47,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=884,
    abilities=[
        Ability(
            title="Hard Coat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Gatling Slug",
            game_text="This attack does 40 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.METAL), 40, base=10),
        ),
    ],
)