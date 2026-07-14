from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.session.passives import Passive, effective_max_hp


class IceFacePassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.target is not carrier:
            return
        if carrier.get_attribute(AttrID.HP, 0) < effective_max_hp(calc.board, carrier):
            return
        calc.amount = max(0, calc.amount - 60)

card = PokemonCardDef(
    guid="d0dddfa3-a086-535a-ab9c-3156ef0e3098",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Eiscue"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SWSH2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Ability(
            title="Ice Face",
            game_text="If this Pok\u00e9mon has full HP, it takes 60 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=IceFacePassive(),
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=spread_damage(10, side="opponent", also_base=True),
        ),
    ],
)